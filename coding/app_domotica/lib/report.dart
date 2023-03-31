class Report {
  final String id;
  final int co2;
  final double temperature;
  final double humidity;
  final DateTime date;
  final int internalLight;
  final int externalLight;
  final int nPeople;

  const Report({
    required this.id,
    required this.co2,
    required this.temperature,
    required this.humidity,
    required this.date,
    required this.internalLight,
    required this.externalLight,
    required this.nPeople,
  });

  factory Report.fromJson(Map<String, dynamic> json) {
    return Report(
      id: json['id'] ?? '',
      co2: json['co2'] ?? 0,
      temperature: json['temperature'] ?? 0,
      humidity: json['humidity'] ?? 0,
      date: DateTime.tryParse(json['date'] ?? '') ?? DateTime.now(),
      internalLight: json['internalLight'] ?? 0,
      externalLight: json['externalLight'] ?? 0,
      nPeople: json['nPeople'] ?? 0,
    );
  }
}
