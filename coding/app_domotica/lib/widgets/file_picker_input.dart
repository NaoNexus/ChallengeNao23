import 'dart:io';

import 'package:path/path.dart' as path;

import 'package:co2_sensor_app/app_colors.dart';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';

class FilePickerInput extends StatefulWidget {
  const FilePickerInput({
    Key? key,
    this.initialFile,
    this.validator,
    this.acceptedExtensions = const ['.pdf'],
    this.onSelected,
  }) : super(key: key);

  final File? initialFile;
  final List<String> acceptedExtensions;

  final String? Function(File? file)? validator;
  final Function(File? file)? onSelected;

  @override
  State<FilePickerInput> createState() => _FilePickerInputState();
}

class _FilePickerInputState extends State<FilePickerInput> {
  @override
  Widget build(BuildContext context) {
    return FormField<File>(
      validator: widget.validator,
      initialValue: widget.initialFile,
      builder: (FormFieldState<File> state) {
        return SizedBox(
          child: AnimatedSize(
            duration: const Duration(milliseconds: 200),
            child: Column(
              children: [
                Container(
                  padding: EdgeInsets.zero,
                  margin: EdgeInsets.zero,
                  decoration: BoxDecoration(
                    border: Border.all(
                      color: AppColors.blue,
                    ),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  clipBehavior: Clip.antiAlias,
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      TextButton(
                        style: TextButton.styleFrom(
                          backgroundColor: AppColors.blue,
                          padding: const EdgeInsets.all(12.0),
                          textStyle: const TextStyle(fontSize: 20),
                        ),
                        onPressed: () async {
                          FilePickerResult? selectedFiles =
                              await FilePicker.platform.pickFiles(
                            type: FileType.custom,
                            allowedExtensions: ['pdf'],
                          );

                          if (selectedFiles == null ||
                              selectedFiles.files.isEmpty) {
                            return;
                          }

                          if (selectedFiles.files[0].path == null) return;

                          setState(() {
                            File selectedFile =
                                File(selectedFiles.files[0].path!);
                            state.didChange(selectedFile);
                            if (widget.onSelected != null) {
                              widget.onSelected!(selectedFile);
                            }
                          });
                        },
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(
                              Icons.insert_drive_file_outlined,
                              color: AppColors.blue.withLightness(0.85),
                            ),
                            const SizedBox(
                              width: 8,
                            ),
                            Text(
                              'SELECT PDF',
                              style: TextStyle(
                                fontSize: 20,
                                fontWeight: FontWeight.bold,
                                color: AppColors.blue.withLightness(0.85),
                                letterSpacing: 1.5,
                              ),
                            ),
                          ],
                        ),
                      ),
                      if (state.value != null)
                        Padding(
                          padding: const EdgeInsets.all(8),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(
                                Icons.insert_drive_file_outlined,
                                color: AppColors.blue.withLightness(0.85),
                              ),
                              const SizedBox(width: 8),
                              Flexible(
                                child: Text(
                                  path.basename(state.value!.path),
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(
                                    color: AppColors.blue.withLightness(0.85),
                                  ),
                                ),
                              ),
                              IconButton(
                                icon: const Icon(
                                  Icons.cancel_outlined,
                                  color: Colors.red,
                                ),
                                onPressed: () {
                                  setState(() {
                                    state.didChange(null);
                                    if (widget.onSelected != null) {
                                      widget.onSelected!(null);
                                    }
                                  });
                                },
                              ),
                            ],
                          ),
                        ),
                    ],
                  ),
                ),
                if (state.hasError)
                  Padding(
                    padding:
                        const EdgeInsets.symmetric(vertical: 8, horizontal: 12),
                    child: Row(
                      children: [
                        Text(
                          state.errorText ?? '',
                          style: TextStyle(
                            fontSize: 12,
                            color: Theme.of(context).colorScheme.error,
                          ),
                        ),
                      ],
                    ),
                  ),
              ],
            ),
          ),
        );
      },
    );
  }
}
