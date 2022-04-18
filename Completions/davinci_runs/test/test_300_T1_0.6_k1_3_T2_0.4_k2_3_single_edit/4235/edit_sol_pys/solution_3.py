import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class File {
	public static void main(String[] args) {
		File file = new File("/Users/mkyong/filename.txt");
		FileReader fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);

		String line;
		try {
			while ((line = br.readLine()) != null) {
				System.out.println(line);
			}
			br.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
