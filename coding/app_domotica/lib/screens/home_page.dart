import 'package:co2_sensor_app/api.dart';
import 'package:co2_sensor_app/report.dart';
import 'package:environment_sensors/environment_sensors.dart';
import 'package:co2_sensor_app/app_colors.dart';
import 'package:co2_sensor_app/send_popup.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key, required this.api});

  final Api api;

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
        backgroundColor: AppColors.bgcolor,
        appBar: AppBar(
          title: const Text('CO2 Sensor App'),
          backgroundColor: AppColors.teal,
        ),
        floatingActionButton: FloatingActionButton.extended(
          onPressed: () {
            showDialog(
              context: context,
              barrierDismissible: true,
              builder: (context) => SendPopup(
                api: widget.api,
              ),
            );
          },
          backgroundColor: AppColors.orange,
          label: const Text('NEW REPORT'),
          icon: const Icon(Icons.add),
        ),
        body: Center(
          child: FutureBuilder<List<Report>>(
            future: widget.api.getReports(),
            builder: (context, snapshot) {
              if (snapshot.hasData) {
                return ListView(
                  physics: const AlwaysScrollableScrollPhysics(),
                  children: snapshot.data!
                      .map(
                        (report) => Container(
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(8),
                            color: AppColors.bgcolor,
                          ),
                          child: Card(
                            elevation: 5,
                            color: AppColors.cardbgcolor,
                            margin: const EdgeInsets.all(10),
                            child: ListBody(
                              children: [
                                ListTile(
                                  title: Text(
                                    '${report.date.day}/${report.date.month}/${report.date.year}  ${report.date.hour}:${report.date.minute}',
                                    style: const TextStyle(
                                      fontSize: 25,
                                      color: AppColors.textcolor,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  subtitle: Text(
                                    report.id,
                                    style: const TextStyle(
                                      fontSize: 10,
                                      color: AppColors.textcolor,
                                    ),
                                  ),
                                ),
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  children: [
                                    Expanded(
                                      child: Padding(
                                        padding: const EdgeInsets.only(
                                          left: 30,
                                        ),
                                        child: Column(
                                          crossAxisAlignment:
                                              CrossAxisAlignment.start,
                                          children: [
                                            Row(
                                              children: [
                                                const Icon(
                                                  Icons.people,
                                                  color: AppColors.orange,
                                                ),
                                                Text(
                                                  ' ${report.nPeople}',
                                                  style: const TextStyle(
                                                    color: AppColors.textcolor,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                              ],
                                            ),
                                            const SizedBox(height: 2),
                                            Row(
                                              children: [
                                                const Icon(
                                                  Icons.thermostat_outlined,
                                                  color: AppColors.orange,
                                                ),
                                                Text(
                                                  ' ${report.temperature}°C',
                                                  style: const TextStyle(
                                                    color: AppColors.textcolor,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                              ],
                                            ),
                                            const SizedBox(height: 2),
                                            Row(
                                              mainAxisAlignment:
                                                  MainAxisAlignment.start,
                                              children: [
                                                const Icon(
                                                  Icons.water_outlined,
                                                  color: AppColors.orange,
                                                ),
                                                Text(
                                                  ' ${report.humidity}%',
                                                  style: const TextStyle(
                                                    color: AppColors.textcolor,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                              ],
                                            ),
                                            const SizedBox(height: 2),
                                          ],
                                        ),
                                      ),
                                    ),
                                    Expanded(
                                      child: Padding(
                                        padding: const EdgeInsets.only(
                                          left: 30,
                                        ),
                                        child: Column(
                                          crossAxisAlignment:
                                              CrossAxisAlignment.start,
                                          children: [
                                            Row(
                                              mainAxisAlignment:
                                                  MainAxisAlignment.start,
                                              children: [
                                                const Icon(
                                                  Icons.co2,
                                                  color: AppColors.orange,
                                                ),
                                                Text(
                                                  ' ${report.co2} ppm',
                                                  style: const TextStyle(
                                                    color: AppColors.textcolor,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                              ],
                                            ),
                                            const SizedBox(height: 2),
                                            Row(
                                              children: [
                                                const Icon(
                                                  Icons.wb_sunny,
                                                  color: AppColors.orange,
                                                ),
                                                Text(
                                                  ' ${report.externalLight} lux',
                                                  style: const TextStyle(
                                                    color: AppColors.textcolor,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                              ],
                                            ),
                                            const SizedBox(height: 2),
                                            Row(
                                              children: [
                                                const Icon(
                                                  Icons.lightbulb_outline,
                                                  color: AppColors.orange,
                                                ),
                                                Text(
                                                  ' ${report.internalLight} lux',
                                                  style: const TextStyle(
                                                    color: AppColors.textcolor,
                                                    fontWeight: FontWeight.bold,
                                                  ),
                                                ),
                                              ],
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(
                                  height: 13,
                                ),
                              ],
                            ),
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
