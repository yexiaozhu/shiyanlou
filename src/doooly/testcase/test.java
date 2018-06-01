package doooly.testcase;

import java.io.IOException;

import org.testng.annotations.Test;
import org.testng.Assert;
import org.testng.Reporter;

import testdooolyapi.Common;
import testdooolyapi.getCityWeather;

public class test {
	public String httpResult = null, weatherinfo = null, city = null, exp_city = null;
	public static String cityCode = "";
	public static getCityWeather weather = new getCityWeather();
	
	@Test(groups = {"BaseCase"})
	public void getSheZhen_Succ() throws IOException{
		exp_city = "����";
		cityCode = "101280601";
		resultCheck(cityCode, exp_city);
	}
	
	@Test(groups = {"BaseCase"})
	public void getBeijing_Succ() throws IOException{
		exp_city = "����";
		cityCode = "101010100";
		resultCheck(cityCode, exp_city);
	}
	
	@Test(groups = {"BaseCase"})
	public void getShangHai_Succ() throws IOException{
		exp_city = "�Ϻ�";
		cityCode = "101020100";
		resultCheck(cityCode, exp_city);
	}

	public void resultCheck(String cityCode_str, String exp_city_str) throws IOException{
		Reporter.log("[��������]����ȡ" + exp_city_str + "�����ɹ���");
		httpResult = weather.getHttpResponse(cityCode_str);
		Reporter.log("�����ַ��" + weather.geturl());
		Reporter.log("���ؽ����" + httpResult);
		System.out.println("httpResult:" + httpResult);
		weatherinfo = Common.getJsonValue(httpResult, "weatherinfo");
		System.out.println("weatherinfo" + weatherinfo);
//		city = Common.getJsonValue(weatherinfo, "city");
		String city = Common.getJsonValue(weatherinfo, "city");
		city = new String(city.getBytes("UTF-8"),"UTF-8");
		
		Reporter.log("���������resultcode => excepted: " + exp_city_str + " ,actual: " + city);
		Assert.assertEquals(city, exp_city_str);
	}
}