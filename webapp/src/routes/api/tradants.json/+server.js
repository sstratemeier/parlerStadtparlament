import fs from 'fs';
import path from 'path';

export async function GET(request) {
  const directoryPath = path.join('src', 'lib', 'data'); // Path to your JSON files
  let jsonObjects = [];

  try {
    // Read the directory contents
    const files = fs.readdirSync(directoryPath);

    // Filter JSON files and read their contents
    jsonObjects = files.filter(file => path.extname(file) === '.json').map(file => {
      const filePath = path.join(directoryPath, file);
      const fileContents = fs.readFileSync(filePath, 'utf8');
      return JSON.parse(fileContents); // Parse and return the JSON object
    });

  } catch (error) {
    return new Response({
      status: 500,
      body: {
        error: 'A server error occurred',
      },
    });
  }

  // Return the array of JSON objects
  return new Response({
    status: 200,
    body: jsonObjects
  });
}