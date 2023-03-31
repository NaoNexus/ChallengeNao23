import 'package:co2_sensor_app/app_colors.dart';
import 'package:co2_sensor_app/utilities.dart';
import 'package:co2_sensor_app/widgets/file_picker_input.dart';
import 'package:environment_sensors/environment_sensors.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:io';

import 'package:co2_sensor_app/api.dart';

class SendPopup extends StatefulWidget {
  const SendPopup({super.key, required this.api});

  final Api api;

  @override
  State<SendPopup> createState() => _SendPopupState();
}

class _SendPopupState extends State<SendPopup> {
  File? _pdf;

  final _environmentSensors = EnvironmentSensors();

  final TextEditingController _nPeopleController = TextEditingController();

  final GlobalKey<FormState> _formKey = GlobalKey();

  @override
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      backgroundColor: AppColors.cardbgcolor,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12.0),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Padding(
            padding: const EdgeInsets.all(18.0),
            child: Form(
              key: _formKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const SizedBox(height: 14),
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
                    cursorColor: AppColors.textcolor,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(8),
                        borderSide: const BorderSide(
                            color: AppColors.textcolor, width: 1),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(8),
                        borderSide: const BorderSide(
                            color: AppColors.textcolor, width: 1),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(8),
                        borderSide: const BorderSide(
                            color: AppColors.textcolor, width: 1),
                      ),
                      label: const Text(
                        'Number of people in the room',
                        style: TextStyle(
                          color: AppColors.textcolor,
                        ),
                      ),
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
                      backgroundColor: AppColors.red,
                      padding: const EdgeInsets.all(16.0),
                      textStyle: const TextStyle(fontSize: 20),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8),
                      ),
                    ),
                    onPressed: () async {
                      double light = 0;
                      if (await _environmentSensors
                          .getSensorAvailable(SensorType.Light)) {
                        light = await _environmentSensors.light.first;
                      }
                      if (context.mounted) {
                        if (!_formKey.currentState!.validate()) return;

                        try {
                          widget.api.postFile(
                              context,
                              _pdf!.path,
                              int.parse(_nPeopleController.text),
                              light.round());
                          showSnackBar(
                            context: context,
                            text:
                                'Sent to ip: ${widget.api.ip} on port: ${widget.api.port}  light $light',
                            color: Colors.green,
                            icon: Icons.check,
                          );
                          Navigator.pop(context);
                        } catch (e) {
                          showSnackBar(
                            context: context,
                            text: e.toString(),
                            color: AppColors.red,
                            icon: Icons.error_outline,
                          );
                        }
                      }
                    },
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          'SUBMIT',
                          style: TextStyle(
                            fontSize: 20,
                            fontWeight: FontWeight.bold,
                            color: AppColors.red.withLightness(0.85),
                            letterSpacing: 1.5,
                          ),
                        ),
                        const SizedBox(
                          width: 8,
                        ),
                        Icon(
                          Icons.cloud_upload_outlined,
                          color: AppColors.red.withLightness(0.85),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
