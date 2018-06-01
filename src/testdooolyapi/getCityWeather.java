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
		// 建立实际连接
		Connection.connect();
//		out = new DataOutputStream(Connection.getOutputStream());
		// 创建一个新的数据输出流， 将数据写入知道基础输出流。
//		out.flush();
		// 清空此数据输出流
//		out.close();
		BufferedReader reader = new BufferedReader(new InputStreamReader(Connection.getInputStream(), "UTF-8"));
		while ((line = reader.readLine()) != null) {
			httpResults = httpResults + line.toString();
		}
		reader.close(); // 关闭该流并释放与之关联的资源
		Connection.disconnect(); // 断开连接
		} catch (Exception e) {
			e.printStackTrace();
		}
		return httpResults;
	}
}
