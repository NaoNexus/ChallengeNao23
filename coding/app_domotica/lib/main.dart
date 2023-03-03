import 'package:co2_sensor_app/app_colors.dart';
import 'package:co2_sensor_app/screens/home_page.dart';
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
      home: const HomePage(),
      theme: ThemeData.from(
        colorScheme: ColorScheme.fromSeed(seedColor: AppColors.blue),
      ),
    );
  }
}
