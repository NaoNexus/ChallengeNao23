import 'dart:convert';
import 'dart:developer';

import 'package:co2_sensor_app/report.dart';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Api {
  String ip;
  int? port;

  Api({required this.ip, this.port});

  String get address => '$ip${port != null ? ':$port' : ''}';

  void postFile(
      BuildContext context, String path, int numberOfPeople, int light) async {
    try {
      http.MultipartRequest request =
          http.MultipartRequest('POST', Uri.http(address, 'api/pdf_report'))
            ..files.add(await http.MultipartFile.fromPath('file', path))
            ..fields['nPeople'] = numberOfPeople.toString()
            ..fields['internalLight'] = light.toString();

      log(request.url.toString());

      await request.send();
    } catch (e) {
      log(e.toString());
    }
  }

  Future<List<Report>> getReports() async {
    final response = await http.get(Uri.http(address, 'api/reports'));

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
}
