import 'package:co2_sensor_app/home_page.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Co2 Sensor App',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Co2 Sensor App'),
        ),
        body: const HomePage(),
      ),
    );
  }
}
