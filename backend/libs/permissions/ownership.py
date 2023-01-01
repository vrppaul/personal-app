from core.models import OwnershipModel
from libs.permissions.base import ModelObjectPermissionBase, PermissionException
from users.models import User


def is_owner(user: User, model_object: OwnershipModel) -> bool:
    """Simply checks the ownership of the object by checking the ``owner`` attribute of the object.

    :param user: the one to be checked against the owner of the object
    :param model_object: models.Model object, which should have ``owner`` attribute.
    :return: bool flag.
    """
    if not hasattr(model_object, "owner"):
        raise AttributeError(f"Model {type(model_object)} does not have 'owner' attribute.")

    return user == model_object.owner


class IsOwner(ModelObjectPermissionBase):
    def check_object(self, model_object: OwnershipModel, *args, **kwargs) -> None:
        if not is_owner(self.request.user, model_object):
            raise PermissionException("User is not the owner of the object")
