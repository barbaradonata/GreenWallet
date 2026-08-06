const https = require('https');
const fs = require('fs');

const files = [
  { name: 'dashboard.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmE5NzQ3OTgwNDMxMWFjYWE3MmMxZjkyEgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'login.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmE2YjFiZDYwNjM5NDJlOTQyMTBhMTEzEgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'comando-de-voz.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmFhZGNiMzMwNDMxMWFjYWE3MmMxZjkyEgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'pesquisa.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmEzY2YxZjAwMzRhNGVhYTI0MGM0OTJiEgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'categorias.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmE4ZjM5YmQwMzM4NTc1NDI5MGFmNTcyEgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'calendario.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmExNzM0YWIwMmE5ODFmMDQ0MjdiNGY4EgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'nova-despesa.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmEwOWM2ZTcwMWE2MDk0YWFmMjhiMGRiEgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'metas.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmEyOWM0NmIwMWE2Mzg2MGU3MGIyZTI1EgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' },
  { name: 'index.html', url: 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ7Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpaCiVodG1sXzAwMDY1NzRmZmE3NzM1MWUwMGRiNDlkZDkxMThjOTVkEgsSBxDK__KDlhsYAZIBIwoKcHJvamVjdF9pZBIVQhM0ODc1OTU5MTcxNzI0MTkyNDYw&filename=&opi=89354086' }
];

async function download() {
  for (const f of files) {
    await new Promise((resolve, reject) => {
      https.get(f.url, (res) => {
        const file = fs.createWriteStream(f.name);
        res.pipe(file);
        file.on('finish', () => {
          file.close();
          console.log(`Downloaded ${f.name}`);
          resolve();
        });
      }).on('error', (err) => {
        fs.unlink(f.name, () => {});
        console.error(`Error downloading ${f.name}: ${err.message}`);
        resolve();
      });
    });
  }
}

download();
