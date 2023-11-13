import 'content.dart';
import 'list.dart';

void main() {
  User userData = User('john', 'john@gmail.com', 20);
  userData.login();
  print(userData.name);

  SuperUser superUserData = SuperUser('jane', 'jane@gmail.com', 25);
  superUserData.login();
  superUserData.publish();
  print(superUserData.name);

  String name = 'John';
  print('hello ${name}');
  print('hey $name');

  bool isTrue = true;
  print('isTrue is ${isTrue}');

  dynamic x = 'am here';
  print(x);
  x = 123;
  print(x);

  List myList = List(
      title: 'A life of a programmer',
      description:
          'In the land of dev the destiny of programmer depends on his ability to think and code');
  print(myList.title);
  print(myList.description);

  Content myContent = Content();
  print(myContent);
}

// Create a class called User
class User {
  String name;
  String email;
  int age;

// Create a constructor for the User class
  User(this.name, this.email, this.age);

// Create a method called login
  void login() {
    print('User logged in');
  }
}

// Create a class called SuperUser that extends User
class SuperUser extends User {
  // Create a constructor for the SuperUser class
  SuperUser(String name, String email, int age) : super(name, email, age);

  // Create a method called publish
  void publish() {
    print('Published update');
  }
}
