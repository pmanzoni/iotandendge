/*
 * Voice sampler for Arduino Nano 33 BLE Sense by Alan Wang
 * Adapted by https://pmanzoni.github.io, Feb 2021, Dec 2021, ...
 */

#include <math.h>
#include <PDM.h>

#define SERIAL_PLOT_MODE  true  // set to true to test sampler in serial plotter

#define PDM_BUFFER_SIZE   256    // buffer size of PDM mic
#define PDM_SOUND_GAIN    128    // sound gain of PDM mic

#define FEATURE_SIZE      64     // sampling size of one voice instance
#define SAMPLE_DELAY      20     // delay time (ms) between sampling
#define TOTAL_SAMPLE      50     // total number of voice instance

// #define SAMPLE_THRESHOLD  200    // RMS threshold to trigger sampling


double feature_data[FEATURE_SIZE];
unsigned int total_counter = 0;

short sampleBuffer[PDM_BUFFER_SIZE];
volatile int samplesRead;
volatile double rms;
volatile unsigned int sum;

// turns on and off the onboard LED during d msecs, t times
void flashled(int d, int t) {
  for (unsigned short i = 0; i < t; i++) {
    delay(d);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(d);
    digitalWrite(LED_BUILTIN, LOW);
  }
}

// callback function for PDM mic
void onPDMdata() {

  // query the number of bytes available
  int bytesAvailable = PDM.available();

  // read into the sample buffer
  int bytesRead = PDM.read(sampleBuffer, bytesAvailable);

  // 16-bit, 2 bytes per sample
  samplesRead = bytesRead / 2;

  // calculate RMS (root mean square) from sample_buffer
  rms = -1;
  sum = 0;
  for (unsigned short i = 0; i < (samplesRead); i++) 
    sum += pow(sampleBuffer[i], 2);
  rms = sqrt(double(sum) / (double(samplesRead)));
}


void setup() {

  Serial.begin(115200);
  while (!Serial);

  PDM.onReceive(onPDMdata);
  PDM.setBufferSize(PDM_BUFFER_SIZE);
  PDM.setGain(PDM_SOUND_GAIN);

  // start PDM mic and sampling at 16 KHz
  if (!PDM.begin(1, 16000)) {  
    Serial.println("Failed to start PDM!");
    while (1);
  }

  pinMode(LED_BUILTIN, OUTPUT);

  // wait 1 second to avoid initial PDM reading
  flashled(500, 1);

  if (!SERIAL_PLOT_MODE) Serial.println("# === Voice data start ===");
  
}


void loop() {

  // waiting until sampling triggered
  // while (rms < SAMPLE_THRESHOLD);

  digitalWrite(LED_BUILTIN, HIGH);
  delay(3000);
  digitalWrite(LED_BUILTIN, LOW);
  for (unsigned short i = 0; i < FEATURE_SIZE; i++) {  // sampling
    while (rms < 0);
    feature_data[i] = rms;
    delay(SAMPLE_DELAY);
  }
  digitalWrite(LED_BUILTIN, HIGH);

  if (!SERIAL_PLOT_MODE) Serial.print("[");

  // pring out sampling data
  for (unsigned short i = 0; i < FEATURE_SIZE; i++) {
    if (!SERIAL_PLOT_MODE) {
      Serial.print(feature_data[i]);
      Serial.print(", ");
    } else {
      Serial.println(feature_data[i]);
    }
  }
  if (!SERIAL_PLOT_MODE) {
    Serial.println("],");
  } else {
    for (unsigned short i = 0; i < (FEATURE_SIZE / 2); i++) Serial.println(0);
  }

  // stop sampling when enough samples are collected
  if (!SERIAL_PLOT_MODE) {
    total_counter++;
    if (total_counter >= TOTAL_SAMPLE) {
      Serial.println("# === Voice data end ===");
      PDM.end();
      while (1) flashled(100, 3);
    }
  }

  // wait for 2 second after one sampling
  flashled(500, 2);

}
