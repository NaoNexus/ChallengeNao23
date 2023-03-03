import 'package:co2_sensor_app/app_colors.dart';
import 'package:flutter/material.dart';

void showSnackBar({
  required BuildContext context,
  required String text,
  IconData? icon,
  Color? color,
}) {
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      backgroundColor: (color ?? AppColors.red).withLightness(0.9),
      content: Row(
        children: [
          if (icon != null) ...[
            Icon(
              icon,
              color: color ?? AppColors.red,
            ),
            const SizedBox(width: 8),
          ],
          Expanded(
            child: Text(
              text,
              textAlign: TextAlign.center,
              style: TextStyle(
                color: color ?? AppColors.red,
              ),
            ),
          ),
        ],
      ),
    ),
  );
}
