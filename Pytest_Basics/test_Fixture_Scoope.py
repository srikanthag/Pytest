# 1. Function Scope (Test Scope)

import pytest

# Define the BankAccount class (simple example)
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def get_balance(self):
        return self.balance

    def reset(self):
        self.balance = 0


@pytest.fixture
def setup_account():
    # Setup: Initialize an account with 0 balance
    account = BankAccount(balance=0)
    yield account  # Provide this account fixture to the test function
    # Teardown: Reset the account after the test
    account.reset()

def test_deposit(setup_account):
    account = setup_account
    account.deposit(100)
    assert account.get_balance() == 100

def test_withdraw(setup_account):
    account = setup_account
    account.deposit(200)
    account.withdraw(50)
    assert account.get_balance() == 150



# ==========================================================================

# 2. Module Scope:

import pytest

# Define the DatabaseConnection class
class DatabaseConnection:
    def __init__(self):
        self.users = []
        self.orders = []

    def connect(self):
        # Simulate connecting to a database
        print("Connected to the database.")

    def disconnect(self):
        # Simulate disconnecting from the database
        print("Disconnected from the database.")

    def insert(self, record):
        # Simulate inserting a record into the database
        if isinstance(record, User):
            self.users.append(record)
        elif isinstance(record, Order):
            self.orders.append(record)

    def find_user(self, name):
        # Find a user by name
        return next((user for user in self.users if user.name == name), None)

    def find_order(self, amount):
        # Find an order by amount
        return next((order for order in self.orders if order.amount == amount), None)

# Define the User class
class User:
    def __init__(self, name):
        self.name = name

# Define the Order class
class Order:
    def __init__(self, user, amount):
        self.user = user
        self.amount = amount

# Define the pytest fixture for the database connection
@pytest.fixture(scope="module")
def setup_database():
    # Setup: Initialize a database connection (once per module)
    db = DatabaseConnection()
    db.connect()
    yield db  # Provide the connection to the tests
    # Teardown: Close the connection after all tests in the module
    db.disconnect()

def test_user_insert(setup_database):
    db = setup_database
    user = User(name="Alice")
    db.insert(user)
    assert db.find_user("Alice") is not None

def test_order_insert(setup_database):
    db = setup_database
    order = Order(user="Alice", amount=200)
    db.insert(order)
    assert db.find_order(200) is not None

# ==========================================================================

# 3. Class Scope:

import pytest

# Define the User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def login(self):
        # Simulate a login by setting logged_in to True
        self.logged_in = True
        return self.logged_in

    def logout(self):
        # Simulate logout by setting logged_in to False
        self.logged_in = False

    def is_logged_in(self):
        return self.logged_in

    def delete(self):
        # Simulate deleting the user
        print(f"User {self.username} deleted.")

# Define the fixture with scope "class"
@pytest.fixture(scope="class")
def setup_user():
    # Setup: Create a user instance for all tests in the class
    user = User(username="testuser", password="password123")
    yield user  # Provide the user instance to the tests
    # Teardown: Delete user data after all tests in the class
    user.delete()

# Define test cases for user authentication
class TestUserAuthentication:
    def test_login(self, setup_user):
        user = setup_user
        assert user.login() == True

    def test_logout(self, setup_user):
        user = setup_user
        user.logout()
        assert user.is_logged_in() == False

# ==========================================================================

# 4. Session Scope

import pytest

# Define the Microservice class
class Microservice:
    def __init__(self):
        self.features = {
            "Feature 1": True,
            "Feature 2": False
        }

    def start(self):
        # Simulate starting the service
        print("Microservice started.")

    def stop(self):
        # Simulate stopping the service
        print("Microservice stopped.")

    def is_feature_enabled(self, feature):
        return self.features.get(feature, False)


# Define the pytest fixture with session scope
@pytest.fixture(scope="session")
def setup_service():
    # Setup: Start a microservice (once per session)
    service = Microservice()
    service.start()
    yield service  # Provide the service to all tests
    # Teardown: Stop the service after all tests in the session are done
    service.stop()


# Define the test cases
def test_feature_1(setup_service):
    service = setup_service
    assert service.is_feature_enabled("Feature 1")


def test_feature_2(setup_service):
    service = setup_service
    assert service.is_feature_enabled("Feature 2")

