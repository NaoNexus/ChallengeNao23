import 'package:http/http.dart' as http;

class Api {
  String ip;
  int? port;

  Api({required this.ip, this.port});

  String get address => '$ip${port != null ? ':$port' : ''}';

  void postFile(String path, int numberOfPeople, int light) async {
    http.MultipartRequest request =
        http.MultipartRequest('POST', Uri.parse('http://' + address))
          ..files.add(await http.MultipartFile.fromPath('pdf', path))
          ..fields['numberPeople'] = numberOfPeople.toString()
          ..fields['internalLight'] = light.toString();
    await request.send();
  }
}
