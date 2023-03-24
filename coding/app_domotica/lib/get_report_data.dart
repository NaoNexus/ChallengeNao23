import 'dart:convert';
import 'package:http/http.dart' as http;

Future<List<Report>> getReports() async {
  final response =
      await http.get(Uri.parse('http://192.168.0.150:5000/api/reports'));

  if (response.statusCode == 200) {
    List<Report> reports = [];

    for (Map<String, dynamic> report in jsonDecode(response.body)['data']) {
      reports.add(Report.fromJson(report));
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
  final double humidity;
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
      id: json['id'] ?? '',
      co2: json['co2'] ?? 0,
      temperature: json['temperature'] ?? 0,
      humidity: json['humidity'] ?? 0,
      date: DateTime.tryParse(json['date'] ?? '') ?? DateTime.now(),
      internalLight: json['internalLight'] ?? 0,
      externalLight: json['externalLight'] ?? 0,
      nPeople: json['nPeople'] ?? 0,
    );
  }
}
