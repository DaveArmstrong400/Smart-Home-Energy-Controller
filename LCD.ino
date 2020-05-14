// LCD display to replicate the digital display found in most domestic meters.
// Coded to run through seven readings, one for each day of a week. These
// will be the total usage and therefore would need processing to find
// the daily usage.

//----------------------------------------------------------------------------------------------------------
// Add libraries from open source documents
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <LiquidCrystal.h>

LiquidCrystal_I2C lcd(0x27,20,4);                   // set the LCD address to 0x27 for a 20 chars and 4 line display

//----------------------------------------------------------------------------------------------------------
//Begin LCD setup and program

void setup()
{
  lcd.init();                                       // initialise the lcd 
  lcd.init();
                                   
  lcd.backlight();                                  // start backlight for display
  lcd.setCursor(0,0);                               // set cursor point to begin text, line 0, character 0
  lcd.print("--------------------"); 
  lcd.setCursor(0,1);
  lcd.print("Welcome to my Demo:");                 // display welcome message
  lcd.setCursor(1,2);
  lcd.print("Smart Home Energy");
  lcd.setCursor(5,3);
  lcd.print("Controller");
  delay(5000);                                      // hold welcome message for 5 seconds

  lcd.clear();                                      // clear the lcd display
  delay(2000);
  
  lcd.setCursor(6,1);
  lcd.print("1OOO kWh");                             // print meter reading and units
  delay(2000);
  
  lcd.setCursor(6,1);
  lcd.print("1555 kWh"); 
  delay(10000000); 

  lcd.setCursor(6,1);
  lcd.print("2OOO kWh"); 
  delay(10000); 

  lcd.setCursor(6,1);
  lcd.print("25OO kWh"); 
  delay(10000);   

  lcd.setCursor(6,1);
  lcd.print("3OOO kWh"); 
  delay(10000); 
  
  lcd.clear();
  delay(10000);
  
  lcd.setCursor(2,1);
  lcd.print("Report Time Now!");
  delay(10000); 
}

//----------------------------------------------------------------------------------------------------------
// No continuous loop required for system
void loop()
{

}
