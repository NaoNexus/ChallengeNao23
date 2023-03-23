import 'package:environment_sensors/environment_sensors.dart';
import 'package:co2_sensor_app/app_colors.dart';
import 'package:co2_sensor_app/send_popup.dart';
import 'package:flutter/material.dart';

import '../get_report_data.dart';

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
        body: Center(
          child: FutureBuilder<List<Report>>(
            future: getReports(),
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                return ListView(
                  physics: const AlwaysScrollableScrollPhysics(),
                  children: snapshot.data!
                      .map(
                        (report) => Container(
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(8),
                            color: Colors.grey.shade50,
                          ),
                          child: Column(
                            children: [
                              ListBody(
                                children: [
                                  Text(
                                    'CO2: ${report.co2} ppm',
                                    style: const TextStyle(
                                      color: AppColors.teal,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  Text(
                                    'Temperature: ${report.temperature} °C',
                                    style: const TextStyle(
                                      color: AppColors.teal,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  Text(
                                    'Humidity: ${report.humidity} %',
                                    style: const TextStyle(
                                      color: AppColors.teal,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  Text(
                                    'Date: ${report.date}',
                                    style: const TextStyle(
                                      color: AppColors.teal,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  Text(
                                    'Internal Light: ${report.internalLight} lux',
                                    style: const TextStyle(
                                      color: AppColors.teal,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  Text(
                                    'External Light: ${report.externalLight} lux',
                                    style: const TextStyle(
                                      color: AppColors.teal,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  Text(
                                    'Number of People: ${report.nPeople}',
                                    style: const TextStyle(
                                      color: AppColors.teal,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ),
                      )
                      .toList(),
                );
              } else if (snapshot.hasError) {
                return Text('${snapshot.error}');
              }

              // By default, show a loading spinner.
              return const CircularProgressIndicator();
            },
          ),
        ),
      ),
    );
  }
}
