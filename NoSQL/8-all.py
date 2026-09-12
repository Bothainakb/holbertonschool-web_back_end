#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return all documents in the collection, or an empty list."""
    return list(mongo_collection.find())
