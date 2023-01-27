import 'package:co2_sensor_app/api.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  late Api _appApi;

  @override
  void initState() {
    _appApi = Api(ip: '', port: 5050);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => FocusScope.of(context).unfocus(),
      child: Scaffold(
        appBar: AppBar(
          actions: [
            IconButton(
              icon: const Icon(Icons.settings_outlined, color: Colors.white),
              onPressed: () {
                //TODO: show settings popup with ip and port
              },
            )
          ],
        ),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 50),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: <Widget>[
                const TextField(
                  autofocus: false,
                  decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    hintText: 'Enter number of people in the room',
                  ),
                ),
                const SizedBox(height: 20),
                ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: TextButton(
                    style: TextButton.styleFrom(
                      foregroundColor: Colors.black,
                      backgroundColor: Colors.red,
                      padding: const EdgeInsets.all(16.0),
                      textStyle: const TextStyle(fontSize: 20),
                    ),
                    onPressed: () {}, //TODO: call send server data class
                    child: const Text('SUBMIT'),
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
