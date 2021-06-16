import boto3
from chalice import Chalice

app = Chalice(app_name='indiecollab-emails')


def get_app_db():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('indiecollabemails')
    return table

@app.route('/email', methods=['POST'], cors=True)
def input_email():
    email_as_json = app.current_request.json_body
    table = get_app_db()
    try:
        table.put_item(Item=email_as_json)
        return {'message': 'success', 'status': 201}
    except Exception as e:
        return {'message': str(e)}