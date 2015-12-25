# https://docs.mongodb.org/getting-started/python/client/
# getting started with PyMongo


from pymongo import MongoClient
from datetime import datetime


def get_db():
    client = MongoClient('localhost:27017')
    db = client.test
    return db


def add_country(db):
    db.countries.insert({"name": "Canada"})


def get_country(db):
    return db.countries.find_one()


def find_restaurant(prop, matched):
    """
    根据参数和参数值查找旅馆
    Args:
        prop:
        matched:

    Returns:

    """
    db = get_db()
    cursor = db.restaurants.find({prop: matched})
    count = 0
    for document in cursor:
        print("Found→", document)
        count += 1
    print("%5d record(s) found." % count)


def find_restaurant_Combine(**kwargs):
    """
    根据参数和参数值查找旅馆
    Args:
        prop:
        matched:

    Returns:
        object:
    """
    logical = kwargs["logical"]
    conditions = kwargs["conditions"]
    db = get_db()
    cursor = db.restaurants.find({logical: conditions})
    count = 0
    for document in cursor:
        print("Found→", document)
        count += 1
    print("%5d record(s) found." % count)


def insert_restaurant(db):
    """
    插入一家旅馆
    Args:
        db:

    Returns:
        The operation returns an InsertOneResult object, which includes an attribute inserted_id
        that contains the _id of the inserted document.

    """
    db = get_db()
    collRestaurants = db.restaurants
    result = db.restaurants.insert_one(
            {
                "address": {
                    "street": "3 居家桥路",
                    "zipcode": "10075",
                    "building": "1480",
                    "coord": [-73.9557413, 40.7720266]
                },
                "borough": "浦东",
                "cuisine": "中国",
                "grades": [
                    {
                        "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                        "grade": "A",
                        "score": 11
                    },
                    {
                        "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                        "grade": "B",
                        "score": 17
                    }
                ],
                "name": "小雪",
                "restaurant_id": "41704622"
            }
    )
    return result.inserted_id


if __name__ == "__main__":
    # Insert data
    # try:
    #     result = insert_restaurant()
    # except Exception as err:
    #     print(err)
    # else:
    #     print(result.inserted_id)

    # # Find data
    # # Query by a Top Level Field
    # find_restaurant("name", "小雪")
    # # Query by a Field in an Embedded Document
    # find_restaurant("address.zipcode", "10075")
    # # Query by a Field in an Array
    # find_restaurant("grades.grade", "D")
    # # Specify Conditions with Operators
    # find_restaurant("grades.score", {"$gt": 30})
    # # Combine Conditions
    # find_restaurant_Combine(logical="$and", conditions=[{"cuisine": "Italian"}, {"address.zipcode": "10075"}])
    # # find_restaurant_Combine(logical="$or", conditions=[{"cuisine": "Italian"}, {"address.zipcode": "10075"}])

    # Update data
    # You can use the update_one() and the update_many() methods to update documents of a collection. The update_one() method updates a single document. Use update_many() to update all documents that match the criteria. The methods accept the following parameters:
    #
    # a filter document to match the documents to update,
    # an update document to specify the modification to perform, and
    # an optional upsert parameter.
    db = get_db()

    # Update Top-Level Fields
    result = db.restaurants.update_one(
            {"name": "Juni"},
            {
                "$set": {
                    "cuisine": "American (New)"
                },
                "$currentDate": {"lastModified": True}
            }
    )
    print(result.matched_count, result.modified_count)

    # Update an Embedded Field
    result = db.restaurants.update_one(
            {"restaurant_id": "41156888"},
            {"$set": {"address.street": "East 31st Street"}}
    )
    print(result.matched_count, result.modified_count)

    # Update Multiple Documents
    result = db.restaurants.update_many(
            {"address.zipcode": "10016", "cuisine": "Other"},
            {
                "$set": {"cuisine": "Category To Be Determined"},
                "$currentDate": {"lastModified": True}
            }
    )
    print(result.matched_count, result.modified_count)

    # Replace a Document
    result = db.restaurants.replace_one(
            {"restaurant_id": "41704620"},
            {
                "name": "Vella 2",
                "address": {
                    "coord": [-73.9557413, 40.7720266],
                    "building": "1480",
                    "street": "2 Avenue",
                    "zipcode": "10075"
                }
            }
    )
    print(result.matched_count, result.modified_count)
  