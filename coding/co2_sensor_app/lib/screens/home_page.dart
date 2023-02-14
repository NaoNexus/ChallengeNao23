import 'package:environment_sensors/environment_sensors.dart';
import 'package:co2_sensor_app/app_colors.dart';
import 'package:co2_sensor_app/send_popup.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final environmentSensors = EnvironmentSensors();

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => FocusScope.of(context).unfocus(),
      child: Scaffold(
        appBar: AppBar(
          title: const Text('CO2 Sensor App'),
        ),
        floatingActionButton: FloatingActionButton.extended(
          onPressed: () {
            showDialog(
              context: context,
              barrierDismissible: true,
              builder: (context) => const SendPopup(),
            );
          },
          backgroundColor: AppColors.teal,
          label: const Text('NEW REPORT'),
          icon: const Icon(Icons.add),
        ),
      ),
    );
  }
}
