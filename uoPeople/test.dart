void main() {
  User userData = User('john', 'john@gmail.com', 20);
  userData.login();
  print(userData.name);

  SuperUser superUserData = SuperUser('jane', 'jane@gmail.com', 25);
  superUserData.login();
  superUserData.publish();
  print(superUserData.name);
}

class User {
  String name;
  String email;
  int age;

  User(this.name, this.email, this.age);

  void login() {
    print('User logged in');
  }
}

class SuperUser extends User {
  SuperUser(String name, String email, int age) : super(name, email, age);

  void publish() {
    print('Published update');
  }
}
