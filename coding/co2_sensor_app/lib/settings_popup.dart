import 'package:co2_sensor_app/app_colors.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class SettingsPopup extends StatefulWidget {
  const SettingsPopup({
    super.key,
    required this.onValuesSubmitted,
    required this.ip,
    required this.port,
  });

  final Function(String, String) onValuesSubmitted;
  final String ip, port;

  @override
  State<SettingsPopup> createState() => _SettingsPopupState();
}

class _SettingsPopupState extends State<SettingsPopup> {
  final _formKey = GlobalKey<FormState>();
  final _ipController = TextEditingController();
  final _portController = TextEditingController();

  @override
  void initState() {
    _ipController.text = widget.ip;
    _portController.text = widget.port;
    super.initState();
  }

  @override
  void dispose() {
    _ipController.dispose();
    _portController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8.0),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextFormField(
                autofocus: false,
                controller: _ipController,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'IP cannot be empty';
                  }
                  return null;
                },
                decoration: InputDecoration(
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(8),
                  ),
                  label: const Text('IP Address'),
                ),
              ),
              const SizedBox(height: 16.0),
              TextFormField(
                autofocus: false,
                controller: _portController,
                keyboardType: TextInputType.number,
                inputFormatters: [
                  FilteringTextInputFormatter.allow(
                    RegExp(r'\d+'),
                  ),
                ],
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Port cannot be empty';
                  }
                  return null;
                },
                decoration: InputDecoration(
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(8),
                  ),
                  label: const Text('Port'),
                ),
              ),
              const SizedBox(height: 16.0),
              Row(
                children: [
                  Expanded(
                    child: TextButton(
                      style: TextButton.styleFrom(
                        //backgroundColor: Colors.grey.withLightness(0.85),
                        padding: const EdgeInsets.all(16.0),
                        textStyle: const TextStyle(fontSize: 20),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(8),
                        ),
                      ),
                      onPressed: () {
                        Navigator.pop(context);
                      },
                      child: const Text(
                        'CANCEL',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          color: Colors.grey,
                          letterSpacing: 1.5,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: TextButton(
                      style: TextButton.styleFrom(
                        backgroundColor: AppColors.red.withLightness(0.85),
                        padding: const EdgeInsets.all(16.0),
                        textStyle: const TextStyle(fontSize: 20),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(8),
                        ),
                      ),
                      onPressed: () {
                        if (_formKey.currentState!.validate()) {
                          widget.onValuesSubmitted(
                            _ipController.text,
                            _portController.text,
                          );
                          Navigator.pop(context);
                        }
                      },
                      child: const Text(
                        'SAVE',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          color: AppColors.red,
                          letterSpacing: 1.5,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
