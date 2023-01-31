import 'package:flutter/material.dart';

class SettingsPopup extends StatefulWidget {
  final Function(String, String) onValuesSubmitted;
  const SettingsPopup({super.key, required this.onValuesSubmitted});

  @override
  State<SettingsPopup> createState() => _SettingsPopupState();
}

class _SettingsPopupState extends State<SettingsPopup> {
  final _ipController = TextEditingController();
  final _portController = TextEditingController();
  static String _ip = '';
  static String _port = '';
  bool _isIpEmpty = false;
  bool _isPortEmpty = false;

  @override
  void dispose() {
    _ipController.dispose();
    _portController.dispose();
    super.dispose();
  }

  void _submitValues() {
    if (_ipController.text.isNotEmpty && _portController.text.isNotEmpty) {
      _ip = _ipController.text;
      _port = _portController.text;
      widget.onValuesSubmitted(_ip, _port);
      Navigator.pop(context);
    }

    setState(() {
      if (_ipController.text.isEmpty) {
        _isIpEmpty = true;
      }
      if (_portController.text.isEmpty) {
        _isPortEmpty = true;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
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
                      TextField(
                        controller: _ipController,
                        decoration: InputDecoration(
                          labelText: 'IP',
                          errorText: _isIpEmpty ? 'IP cannot be empty' : null,
                        ),
                      ),
                      const SizedBox(height: 20.0),
                      TextField(
                        controller: _portController,
                        decoration: InputDecoration(
                          labelText: 'Port',
                          errorText:
                              _isPortEmpty ? 'Port cannot be empty' : null,
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
                        onPressed: () {
                          _ipController.clear();
                          _portController.clear();
                          setState(() {
                            _isIpEmpty = false;
                            _isPortEmpty = false;
                          });
                        },
                        child: const Text('CANCEL'),
                      ),
                      TextButton(
                        onPressed: () {
                          _submitValues();
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
    );
  }
}
