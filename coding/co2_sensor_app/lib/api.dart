import 'package:http/http.dart' as http;

class Api {
  String ip;
  int? port;

  Api({required this.ip, this.port});

  String get address => '$ip${port != null ? ':$port' : ''}';

  void postFile(String path, int numberOfPeople) async {
    http.MultipartRequest request =
        http.MultipartRequest('POST', Uri.parse(address))
          ..files.add(await http.MultipartFile.fromPath('pdf', path))
          ..fields['numberPeople'] = numberOfPeople.toString();
    await request.send();
  }
}
