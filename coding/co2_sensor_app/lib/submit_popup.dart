import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';

class SubmitPopup extends StatefulWidget {
  const SubmitPopup({super.key});

  @override
  State<SubmitPopup> createState() => _SubmitPopupState();
}

class _SubmitPopupState extends State<SubmitPopup> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Form(
        key: _formKey,
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: Dialog(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(10.0),
            ),
            child: SizedBox(
              height: 280,
              child: Padding(
                padding: const EdgeInsets.all(20.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    SizedBox(
                      height: 190,
                      child: Column(
                        children: [
                          TextFormField(
                            controller: null,
                            validator: (value) {
                              if (value == null || value.isEmpty) {
                                return 'Port cannot be empty';
                              }
                              return null;
                            },
                            decoration: const InputDecoration(
                              labelText: 'Port',
                            ),
                          ),
                          const SizedBox(height: 40.0),
                          ClipRRect(
                            borderRadius: BorderRadius.circular(20),
                            child: TextButton(
                              style: TextButton.styleFrom(
                                foregroundColor: Colors.black,
                                backgroundColor: Colors.red,
                                padding: const EdgeInsets.all(16.0),
                                textStyle: const TextStyle(fontSize: 20),
                              ),
                              onPressed: () async {
                                final result =
                                    await FilePicker.platform.pickFiles();
                              },
                              child: const Text('SELECT FILE'),
                            ),
                          ),
                        ],
                      ),
                    ),
                    SizedBox(
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          TextButton(
                            onPressed: () {},
                            child: const Text('CANCEL'),
                          ),
                          TextButton(
                            onPressed: () {
                              if (_formKey.currentState!.validate()) {
                                Navigator.pop(context);
                              }
                            },
                            child: const Text('OK'),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ));
  }
}
