import 'dart:io';
import 'package:co2_sensor_app/widgets/file_picker_input.dart';

import 'package:co2_sensor_app/api.dart';
import 'package:co2_sensor_app/app_colors.dart';
import 'package:co2_sensor_app/settings_popup.dart';
import 'package:co2_sensor_app/utilities.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String? _ip;
  int? _port;

  File? _pdf;

  final TextEditingController _nPeopleController = TextEditingController();

  final GlobalKey<FormState> _formKey = GlobalKey();

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => FocusScope.of(context).unfocus(),
      child: Scaffold(
        appBar: AppBar(
          title: const Text('CO2 Sensor App'),
          actions: [
            IconButton(
              icon: const Icon(Icons.settings_outlined),
              onPressed: () {
                showDialog(
                  context: context,
                  barrierDismissible: false,
                  builder: (context) => SettingsPopup(
                    ip: _ip ?? '',
                    port: (_port ?? '').toString(),
                    onValuesSubmitted: (ip, port) {
                      setState(() {
                        _ip = ip;
                        _port = int.parse(port);
                      });
                      showSnackBar(
                        context: context,
                        text: 'Connection parameters saved successfully',
                        color: Colors.green,
                        icon: Icons.save_outlined,
                      );
                    },
                  ),
                );
              },
            ),
          ],
        ),
        body: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 50),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const SizedBox(height: 16),
                TextFormField(
                  controller: _nPeopleController,
                  keyboardType: TextInputType.number,
                  inputFormatters: [
                    FilteringTextInputFormatter.allow(
                      RegExp(r'\d+'),
                    ),
                  ],
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Number of people cannot be empty';
                    }
                    return null;
                  },
                  decoration: InputDecoration(
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(8),
                    ),
                    label: const Text('Number of people in the room'),
                  ),
                ),
                const SizedBox(height: 16),
                FilePickerInput(
                  initialFile: _pdf,
                  validator: (file) {
                    if (file == null) return "File cannot be empty";
                    return null;
                  },
                  onSelected: (file) {
                    _pdf = file;
                  },
                ),
                const SizedBox(height: 16),
                TextButton(
                  style: TextButton.styleFrom(
                    backgroundColor: AppColors.red.withLightness(0.85),
                    padding: const EdgeInsets.all(16.0),
                    textStyle: const TextStyle(fontSize: 20),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(8),
                    ),
                  ),
                  onPressed: () {
                    if (!_formKey.currentState!.validate()) return;
                    Api appApi = Api(ip: _ip!, port: _port!);
                    showSnackBar(
                      context: context,
                      text: 'Sent to ip: $_ip on port: $_port',
                      color: Colors.green,
                      icon: Icons.check,
                    );
                  },
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: const [
                      Text(
                        'SUBMIT',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          color: AppColors.red,
                          letterSpacing: 1.5,
                        ),
                      ),
                      SizedBox(
                        width: 8,
                      ),
                      Icon(
                        Icons.cloud_upload_outlined,
                        color: AppColors.red,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
