package testdooolyapi;

import java.net.HttpURLConnection;
import java.net.URL;

public class URLConnection {
	public static HttpURLConnection getConnection(String url) {
		HttpURLConnection connection = null;
		try {
			// 打开和URL连接
			URL postUrl = new URL(url);
			connection = (HttpURLConnection) postUrl.openConnection();
			connection.setDoOutput(true);
			connection.setDoInput(true);
			connection.setRequestMethod("GET");
			connection.setUseCaches(false);
			connection.setInstanceFollowRedirects(true);
			connection.setRequestProperty("Content-Type", "text/html");
			connection.setRequestProperty("Charset", "utf-8");
			connection.setRequestProperty("Accept-Charset", "utf-8");
		} catch (Exception e) {
			e.printStackTrace();
		}
		return connection;
	}
}
