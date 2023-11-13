import 'dart:convert';
import 'package:http/http.dart' as http;

// Fetching data from an API using the http package and handling errors using async/await

Future<void> fetchUserData() async {
  try {
    var response =
        await http.get(Uri.parse('https://jsonplaceholder.typicode.com/users'));

    if (response.statusCode == 200) {
      List<dynamic> users = jsonDecode(response.body);
      for (var user in users) {
        var name = user['name'];
        var email = user['email'];
        print('Name: $name, Email: $email');
      }
    } else {
      print('Request failed with status: ${response.statusCode}');
    }
  } catch (e) {
    print('You have an error: $e');
  }
}

void main() async {
  await fetchUserData();
}
