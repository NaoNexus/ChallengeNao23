import 'dart:convert';
import 'package:http/http.dart' as http;

Future<List<Report>> getReports() async {
  final response =
      await http.get(Uri.parse('http://192.168.0.150:5000/api/reports/'));

  if (response.statusCode == 200) {
    List<Report> reports = [];

    for (Map<String, dynamic> report in jsonDecode(response.body)['data']) {
      reports.add(Report.fromJson(jsonDecode(response.body)));
    }

    return reports;
  } else {
    throw Exception('${response.statusCode} - Failed to load');
  }
}

class Report {
  final String id;
  final int co2;
  final double temperature;
  final String humidity;
  final DateTime date;
  final int internalLight;
  final int externalLight;
  final int nPeople;

  const Report({
    required this.id,
    required this.co2,
    required this.temperature,
    required this.humidity,
    required this.date,
    required this.internalLight,
    required this.externalLight,
    required this.nPeople,
  });

  factory Report.fromJson(Map<String, dynamic> json) {
    return Report(
      id: json['id'],
      co2: json['co2'],
      temperature: json['temperature'],
      humidity: json['humidity'],
      date: DateTime.parse(json['date']),
      internalLight: json['internalLight'],
      externalLight: json['externalLight'],
      nPeople: json['nPeople'],
    );
  }
}
