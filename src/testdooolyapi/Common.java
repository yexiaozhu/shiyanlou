package testdooolyapi;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import bsh.org.objectweb.asm.Type;

public class Common {

	public static String getJsonValue(String JsonString, String JsonId) {
		String JsonValue = "";
		Integer Json_value = 0;
		if (JsonString == null || JsonString.trim().length() < 1) {
			return null;
		}
		
		try {
			JSONObject obj1 = new JSONObject(JsonString);
			System.out.println("obj1:" + obj1);
			System.out.println("JsonId:" + JsonId);
			System.out.println("obj1.get(JsonId):" + obj1.get(JsonId));
			if(obj1.get(JsonId) instanceof JSONObject ){
				JSONObject obj2 = obj1.getJSONObject(JsonId);
				JsonValue = obj2.toString();
				System.out.println("obj2:" + obj2);
				System.out.println("JsonId:" + JsonId);
				return JsonValue;
			}
			else {
				JsonValue = (String) obj1.getString(JsonId);
				System.out.println("JsonValue:" + JsonValue);
				return JsonValue;
			}
		} catch ( JSONException e) {
		e.printStackTrace();
		// TODO: handle exception
		}
		return JsonValue;
	}
}
