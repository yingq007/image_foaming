"""CRUD operations."""

from model import db, User, Image, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_image(url, lastModified):
    """Create a new image in seed_database."""

    image = Image(
        url=url,
        lastModified=lastModified,
    )

    db.session.add(image)
    db.session.commit()

    return image


def get_images():
    """Return all images."""

    return Image.query.all()

def get_image_by_image_id(image_id):
    """Return an image by primary key."""

    return Image.query.get(image_id)


def create_foaming(image_id, user_id, is_foam):
    """Create and return a new image is foaming or not."""


    foam = Image(image_id=image_id, user_id=user_id,foam=is_foam)

    db.session.query(Image).filter_by(image_id=image_id).update({"foam":is_foam,"user_id":user_id})
    db.session.commit()

    return foam


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
