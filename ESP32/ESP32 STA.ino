#include <WiFi.h>
#include <WiFiClient.h>
#include <FirebaseESP32.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP);

#define FIREBASE_HOST "https://getrssi-default-rtdb.asia-southeast1.firebasedatabase.app/"
#define FIREBASE_AUTH "zSOnSGHLyZxhzeKz8qEt9yaUT4s8IxAxjh0pgm8E"
#define ssid "GUILD KONTRAKAN"
#define password "gegewepe"

FirebaseData firebaseData;

int i = 1;

void handleADC(int i) {
  
  // RSSI data string buffer
  int rss1 = 0; 
  int rss2 = 0;
  int rss3 = 0;
  int rss4 = 0;
  String rssTot = "";
  String formattedDate = "";
  
  // scan network
  int numberOfNetworks = WiFi.scanNetworks(); 
  for (int i = 0; i < numberOfNetworks; i++) {
    if (WiFi.SSID(i) == "ESP32_AP1"){
      rss1 = WiFi.RSSI(i);
    }
    else if (WiFi.SSID(i) == "ESP32_AP2"){
      rss2 = WiFi.RSSI(i);
    }
    else if (WiFi.SSID(i) == "ESP32_AP3"){
      rss3 = WiFi.RSSI(i);
    }
    else if (WiFi.SSID(i) == "ESP32_AP4"){
      rss4 = WiFi.RSSI(i);
    }
  }
  timeClient.update();
  formattedDate = timeClient.getFormattedTime();
  
  rssTot = formattedDate+","+String(rss1)+","+String(rss2)+","+String(rss3)+","+String(rss4);
  
  Firebase.set(firebaseData,"/logData/"+String(i), rssTot);
  Firebase.setInt(firebaseData,"/Realtime/AP_1", rss1);
  Firebase.setInt(firebaseData,"/Realtime/AP_2", rss2);
  Firebase.setInt(firebaseData,"/Realtime/AP_3", rss3);
  Firebase.setInt(firebaseData,"/Realtime/AP_4", rss4);
  Firebase.setInt(firebaseData,"/CountData", i);
  
}

//==============================================================
//                  SETUP
//==============================================================
void setup(void){
  Serial.begin(115200);

  WiFi.begin(ssid, password);     //Connect to your WiFi router
  Serial.println("");
  
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);

  //Set database read timeout to 1 minute (max 15 minutes)
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  //tiny, small, medium, large and unlimited.
  //Size and its write timeout e.g. tiny (1s), small (10s), medium (30s) and large (60s).
  Firebase.setwriteSizeLimit(firebaseData, "tiny");
  
  Serial.println("------------------------------------");
  Serial.println("Terhubung...");

  timeClient.begin();
  timeClient.setTimeOffset(7*3600);
}

//==============================================================
//                     LOOP
//==============================================================
void loop(void){
  handleADC(i);
  i++;
}
