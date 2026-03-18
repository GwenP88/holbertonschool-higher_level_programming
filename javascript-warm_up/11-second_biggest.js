#!/usr/bin/node
const liste = (process.argv.slice(2));
const tab = liste.map((element) => parseInt(element));

if (tab.length === 0 || tab.length === 1) {
  console.log(0);
} else {
  const unique = [...new Set(tab)];
  const n = unique.sort((a, b) => b - a);
  console.log(n[1]);
}
