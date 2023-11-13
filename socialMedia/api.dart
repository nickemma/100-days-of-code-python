import 'dart:convert';
import 'package:http/http.dart' as http;

// Fetching data from an API using the http package and handling errors using Promises
void main() {
  var response =
      http.get(Uri.parse('https://jsonplaceholder.typicode.com/users'));
  response.then((value) {
    print(value.statusCode);
    if (value.statusCode == 200) {
      List<dynamic> users = jsonDecode(value.body);
      for (var user in users) {
        var name = user['name'];
        var city = user['address']['city'];
        var email = user['email'];
        print('Name: $name, City: $city, Email: $email');
      }
    } else {
      print('Request failed with status: ${value.statusCode}');
    }
  }).catchError((error) {
    print('Error: $error');
  });
}
