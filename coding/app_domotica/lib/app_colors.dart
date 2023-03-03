import 'package:flutter/material.dart';

class AppColors {
  static const red = Color(0xFFD9413D);
  static const teal = Color(0xFF368DB3);
  static const blue = Color(0xFF1A2B50);
}

extension WithLightness on Color {
  Color withLightness(double lightness) =>
      HSLColor.fromColor(this).withLightness(lightness).toColor();
}
