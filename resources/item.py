from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

#Resources are external representaiton
#where client or api use.

class Item(Resource):
    #Avoid name changes only price
    parser = reqparse.RequestParser()
    #look at JSON payload or form payload to a specific field, ex. "price"
    parser.add_argument(
        'price',
        type = float,
        required=True,
        help= "This field cannot be left blank"
    )
    parser.add_argument(
        'store_id',
        type = int,
        required=True,
        help= "Every item needs a store_id"
    )


    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item

        # filter() takes two arguments, a filtering function and the list of targets.
        # next() gives us the first item by the filter() function
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # return {'item': item}, 200 if item else 404
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {'message': 'Item not found'}, 404



    def post(self, name):
        # if next(filter(lambda x: x['name'] == name, items), None) is not None:
        #     return {'message': "An item with name '{}' already exists".format(name)}, 400
        #prevent error if Content-Type header is not set.
        #data = request.get_json(force=True)
        #prevent error, it returns None
        #data = request.get_json(silent=True)
        #data = request.get_json()

        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()

        #item = ItemModel(name, data['price'], data['store_id'])
        item = ItemModel(name, **data)

        #items.append(item) # This line was for item[] memory database
        try:
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item."}, 500

        return item.json(), 201



    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        #print(data['something_elase'])
        #data = request.get_json()

        item = ItemModel.find_by_name(name)

        if item is None:
            #item = ItemModel(name, data['price'], data['store_id'])
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all() ]}
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
