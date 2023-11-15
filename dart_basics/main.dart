import 'private.dart';

void main() {
  User userData = User('john', 12);
  userData.login();
  print(userData.name);
  print(userData.age);

// Slightly longer version uses ?: operator.
  String playerName(String? name) => name != null ? name : 'Guest';
  print(playerName('Rolando'));

// Very long version uses if-else statement.
  String playerName2(String? name) {
    if (name != null) {
      return name;
    } else {
      return 'Guest';
    }
  }

  print(playerName2('Rolando'));

  @Todo('Dash', 'Implement this function')
  void doSomething() {
    print('Do something else');
  }

  doSomething();
  var hi = 'Hi 🇩🇰';
  print(hi);
  print('The end of the string: ${hi.substring(hi.length - 1)}');

  var mixer = Mixer();
  mixer.doJump();

  var message = StringBuffer('Dart is fun');
  for (var i = 0; i < 5; i++) {
    message.write('!');
  }
  print(message);
}

class Todo {
  final String who;
  final String what;

  const Todo(this.who, this.what);
}

mixin Jump {
  String jump = 'Jumping...';
}

class Mixer with Jump {
  void doJump() {
    print(jump);
  }
}
