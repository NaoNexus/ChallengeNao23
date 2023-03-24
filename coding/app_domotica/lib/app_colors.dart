import 'package:flutter/material.dart';

class AppColors {
  static const red = Color(0xFFD9413D);
  static const teal = Color(0xFF368DB3);
  static const blue = Color(0xFF1A2B50);
  static const orange = Color(0xFFEC8F2D);
  static const bgcolor = Color(0xFF0B2D39);
  static const cardbgcolor = Color(0xFF0F3C4C);
  static const textcolor = Color(0xFFE9F5F9);
  static const appbarcolor = Color(0xFF);
}

extension WithLightness on Color {
  Color withLightness(double lightness) =>
      HSLColor.fromColor(this).withLightness(lightness).toColor();
}
