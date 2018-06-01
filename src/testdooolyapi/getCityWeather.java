package testdooolyapi;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class getCityWeather {

	private String url = "";
	public String geturl() {
		return url;
	}
	
	public String getHttpResponse(String cityCode) throws IOException{
		String line = "";
		String httpResults = "";
		url= ("http://www.weather.com.cn/data/cityinfo/" + cityCode + ".html");
		try {
			HttpURLConnection Connection = URLConnection.getConnection(url);
//		DataOutputStream out = null;
		// ����ʵ������
		Connection.connect();
//		out = new DataOutputStream(Connection.getOutputStream());
		// ����һ���µ������������ ������д��֪�������������
//		out.flush();
		// ��մ����������
//		out.close();
		BufferedReader reader = new BufferedReader(new InputStreamReader(Connection.getInputStream(), "UTF-8"));
		while ((line = reader.readLine()) != null) {
			httpResults = httpResults + line.toString();
		}
		reader.close(); // �رո������ͷ���֮��������Դ
		Connection.disconnect(); // �Ͽ�����
		} catch (Exception e) {
			e.printStackTrace();
		}
		return httpResults;
	}
}
