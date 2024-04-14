from django.db import models
import datetime
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    """
            This class represents a basic user. \n
            Attributes:
            -----------
            param first_name: Describes first name of the user
            type first_name: str max length=20
            param last_name: Describes last name of the user
            type last_name: str max length=20
            param email: Describes the email of the user
            type email: str, unique, max length=100
            param password: Describes the password of the user
            type password: str
            param created_at: Describes the date when the user was created. Can't be changed.
            type created_at: int (timestamp)
            param last_login: Describes the date when the user log out last time.
            type updated_at: int (timestamp)
        """
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    email = models.EmailField(max_length=100, unique=True, default=None)
    password = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(editable=False, auto_now=datetime.datetime.now())
    last_login = models.DateTimeField(editable=False, auto_now=datetime.datetime.now())
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username')
    objects = CustomUserManager()

    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user username, user first_name, user last_name,
                 user email, user password, user updated_at, user created_at, user is_active,
                 user is_admin
        """
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of CustomUser object.
        :return: class, id
        """
        return f"{CustomUser.__name__}(id={self.id})"

    @staticmethod
    def get_by_id(user_id):
        """
        :param user_id: SERIAL: the id of a user to be found in the DB
        :return: user object or None if a user with such ID does not exist
        """
        custom_user = CustomUser.objects.filter(id=user_id).first()
        return custom_user if custom_user else None

    @staticmethod
    def get_by_email(email):
        """
        Returns user by email
        :param email: email by which we need to find the user
        :type email: str
        :return: user object or None if a user with such ID does not exist
        """
        custom_user = CustomUser.objects.filter(email=email).first()
        return custom_user if custom_user else None

    @staticmethod
    def delete_by_id(user_id):
        """
        :param user_id: an id of a user to be deleted
        :type user_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        user_to_delete = CustomUser.objects.filter(id=user_id).first()
        if user_to_delete:
            CustomUser.objects.filter(id=user_id).delete()
            return True
        return False

    @staticmethod
    def create(email, password, first_name=None, username=None, last_name=None):
        """
        :param first_name: first name of a user
        :type first_name: str
        :param username: username of a user
        :type username: str
        :param last_name: last name of a user
        :type last_name: str
        :param email: email of a user
        :type email: str
        :param password: password of a user
        :type password: str
        :return: a new user object which is also written into the DB
        """
        if len(first_name) <= 20 and len(username) <= 20 and len(last_name) <= 20 and len(email) <= 100 and len(
                email.split('@')) == 2 and len(CustomUser.objects.filter(email=email)) == 0:
            custom_user = CustomUser(email=email, password=password, first_name=first_name, username=username,
                                     last_name=last_name)
            custom_user.save()
            return custom_user
        return None

    def to_dict(self):
        """
        :return: user id, user username, user first_name, user last_name,
                 user email, user password, user updated_at, user created_at, user is_active
        :Example:
        | {
        |   'id': 8,
        |   'username': 'mn',
        |   'first_name': 'fn',
        |   'last_name': 'ln',
        |   'email': 'ln@mail.com',
        |   'created_at': 1509393504,
        |   'updated_at': 1509402866,
        |   'is_admin': True
        |   'is_active:' True
        | }
        """
        return {'id': self.id,
                'username': f'{self.username}',
                'first_name': f'{self.first_name}',
                'last_name': f'{self.last_name}',
                'email': f'{self.email}',
                'created_at': int(self.created_at.timestamp()),
                'last_login': int(self.last_login.timestamp()),
                'is_admin': self.is_admin,
                'is_active': self.is_active
                }

    def update(self,
               first_name=None,
               last_name=None,
               username=None,
               password=None,
               is_admin=None,
               is_active=None):
        """
        Updates user profile in the database with the specified parameters.\n
        :param first_name: first name of a user
        :type first_name: str
        :param username: username of a user
        :type username: str
        :param last_name: last name of a user
        :type last_name: str
        :param password: password of a user
        :type password: str
        :param is_admin: is_admin state
        :type is_admin: bool
        :param is_active: activation state
        :type is_active: bool
        :return: None
        """
        user_to_update = CustomUser.objects.filter(email=self.email).first()
        if first_name != None and len(first_name) <= 20:
            user_to_update.first_name = first_name
        if last_name != None and len(last_name) <= 20:
            user_to_update.last_name = last_name
        if username != None and len(username) <= 20:
            user_to_update.username = username
        if password != None:
            user_to_update.password = password
        if is_admin != None:
            user_to_update.is_admin = is_admin
        if is_active != None:
            user_to_update.is_active = is_active
        user_to_update.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all users
        """
        return CustomUser.objects.all()

    def is_admin_user(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_perms(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


