from flask import Blueprint, request
from sqlalchemy import select, func

from next_track.db import db
from next_track.models import Tag
from next_track.lib.tags import search_tags

tags = Blueprint("tags", __name__)


@tags.route("/tags")
def get_tags():
    """
    Controller to search for tags based on a search term.
    """
    search = request.args.get("search", "").strip()

    tags = search_tags(search)

    return {"tags": [{"id": tag.id, "name": tag.name} for tag in tags]}
