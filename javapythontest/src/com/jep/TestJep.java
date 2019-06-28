package com.jep;
import java.io.File; 

import jep.*; 
public class TestJep {
	public void testJep() { 
        try{ 
            File pwd = new File("."); 
            Jep jep = new Jep( false, pwd.getAbsolutePath() ); 
            jep.set("test", "value from java"); 
            jep.runScript("test.py"); 
        }catch(Throwable t){ 
            t.printStackTrace(); 
        } 
    } 

    public static void main(String[] args) { 
        new TestJep().testJep(); 
    } 
}