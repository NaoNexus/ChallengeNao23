import 'dart:developer';

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
}
