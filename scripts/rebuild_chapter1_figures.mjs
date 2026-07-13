import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const root = path.resolve(import.meta.dirname, "..");
const dataDir = path.join(root, "assets", "data");
const outDir = path.join(root, "assets", "figures", "chapter01");
fs.mkdirSync(outDir, { recursive: true });

function readTable(name) {
  const [header, ...rows] = fs.readFileSync(path.join(dataDir, name), "utf8").trim().split(/\r?\n/);
  const keys = header.trim().split(/\s+/);
  return rows.map((row) => Object.fromEntries(row.trim().split(/\s+/).map((value, i) => [keys[i], Number(value)])));
}

const all = readTable("shapes.dat");
const class0 = readTable("shapes0.dat");
const class1 = readTable("shapes1.dat");

const esc = (text) => String(text).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");

function svg(width, height, body, label) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="title desc">
  <title id="title">${esc(label)}</title>
  <desc id="desc">${esc(label)}</desc>
  <rect width="100%" height="100%" fill="white"/>
  <style>
    text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #222; }
    .axis { stroke: #333; stroke-width: 2; }
    .grid { stroke: #d9d9d9; stroke-width: 1; }
    .tick { font-size: 16px; }
    .label { font-size: 20px; font-style: italic; }
    .panel { font-size: 18px; }
  </style>
${body}
</svg>`;
}

function scatterPanel({ x, y, data0, data1 = [], xLabel, yLabel, x0, x1, y0, y1, ox, oy, width, height, panelLabel, separator = false }) {
  const left = ox + 62;
  const top = oy + 18;
  const plotWidth = width - 86;
  const plotHeight = height - 76;
  const px = (value) => left + ((value - x0) / (x1 - x0)) * plotWidth;
  const py = (value) => top + plotHeight - ((value - y0) / (y1 - y0)) * plotHeight;
  let body = "";
  for (let i = 0; i <= 4; i++) {
    const gx = left + (i / 4) * plotWidth;
    const gy = top + (i / 4) * plotHeight;
    body += `<line class="grid" x1="${gx}" y1="${top}" x2="${gx}" y2="${top + plotHeight}"/>`;
    body += `<line class="grid" x1="${left}" y1="${gy}" x2="${left + plotWidth}" y2="${gy}"/>`;
  }
  body += `<line class="axis" x1="${left}" y1="${top + plotHeight}" x2="${left + plotWidth}" y2="${top + plotHeight}"/>`;
  body += `<line class="axis" x1="${left}" y1="${top}" x2="${left}" y2="${top + plotHeight}"/>`;
  body += `<text class="label" x="${left + plotWidth / 2}" y="${oy + height - 14}" text-anchor="middle">${esc(xLabel)}</text>`;
  body += `<text class="label" transform="translate(${ox + 20} ${top + plotHeight / 2}) rotate(-90)" text-anchor="middle">${esc(yLabel)}</text>`;
  body += `<text class="panel" x="${ox + width / 2}" y="${oy + height + 18}" text-anchor="middle">${esc(panelLabel)}</text>`;
  for (const point of data0) {
    body += `<circle cx="${px(point[x])}" cy="${py(point[y])}" r="7" fill="white" stroke="#c43c39" stroke-width="3"/>`;
  }
  for (const point of data1) {
    const cx = px(point[x]);
    const cy = py(point[y]);
    body += `<path d="M ${cx - 8} ${cy} H ${cx + 8} M ${cx} ${cy - 8} V ${cy + 8}" stroke="#2866b1" stroke-width="3"/>`;
  }
  if (separator) {
    body += `<line x1="${px(0)}" y1="${py(0)}" x2="${px(10)}" y2="${py(10)}" stroke="#111" stroke-width="3"/>`;
    body += `<text x="${px(6.7)}" y="${py(7.5)}" font-size="18" transform="rotate(-39 ${px(6.7)} ${py(7.5)})">V₃ − V₂ = 0</text>`;
  }
  return body;
}

let body = "";
const panelWidth = 560;
const panelHeight = 390;
body += scatterPanel({ x: "S", y: "T", data0: all, xLabel: "V₁", yLabel: "V₄", x0: 2.5, x1: 4.5, y0: -0.15, y1: 1.15, ox: 0, oy: 0, width: panelWidth, height: panelHeight, panelLabel: "(a) V₄ vs. V₁" });
body += scatterPanel({ x: "W", y: "T", data0: all, xLabel: "V₂", yLabel: "V₄", x0: 0, x1: 10, y0: -0.15, y1: 1.15, ox: panelWidth, oy: 0, width: panelWidth, height: panelHeight, panelLabel: "(b) V₄ vs. V₂" });
body += scatterPanel({ x: "H", y: "T", data0: all, xLabel: "V₃", yLabel: "V₄", x0: 0, x1: 10, y0: -0.15, y1: 1.15, ox: panelWidth * 2, oy: 0, width: panelWidth, height: panelHeight, panelLabel: "(c) V₄ vs. V₃" });
fs.writeFileSync(path.join(outDir, "scatter-individual.svg"), svg(panelWidth * 3, panelHeight + 36, body, "Scatter plots of V4 against V1, V2, and V3"));

body = "";
body += scatterPanel({ x: "S", y: "W", data0: class0, data1: class1, xLabel: "V₁", yLabel: "V₂", x0: 2.5, x1: 4.5, y0: 0, y1: 10, ox: 0, oy: 0, width: panelWidth, height: panelHeight, panelLabel: "(a) V₂ vs. V₁" });
body += scatterPanel({ x: "W", y: "H", data0: class0, data1: class1, xLabel: "V₂", yLabel: "V₃", x0: 0, x1: 10, y0: 0, y1: 10, ox: panelWidth, oy: 0, width: panelWidth, height: panelHeight, panelLabel: "(b) V₃ vs. V₂" });
body += scatterPanel({ x: "H", y: "S", data0: class0, data1: class1, xLabel: "V₃", yLabel: "V₁", x0: 0, x1: 10, y0: 2.5, y1: 4.5, ox: panelWidth * 2, oy: 0, width: panelWidth, height: panelHeight, panelLabel: "(c) V₁ vs. V₃" });
fs.writeFileSync(path.join(outDir, "scatter-pairs.svg"), svg(panelWidth * 3, panelHeight + 36, body, "Pairwise scatter plots colored by V4 class"));

body = scatterPanel({ x: "W", y: "H", data0: class0, data1: class1, xLabel: "V₂", yLabel: "V₃", x0: 0, x1: 10, y0: 0, y1: 10, ox: 0, oy: 0, width: 720, height: 520, panelLabel: "", separator: true });
fs.writeFileSync(path.join(outDir, "linear-separator.svg"), svg(720, 520, body, "Linear equation separating the two V4 classes"));

function grid(width, height, step = 40) {
  let lines = "";
  for (let x = 20; x <= width - 20; x += step) lines += `<line class="grid" x1="${x}" y1="20" x2="${x}" y2="${height - 20}"/>`;
  for (let y = 20; y <= height - 20; y += step) lines += `<line class="grid" x1="20" y1="${y}" x2="${width - 20}" y2="${y}"/>`;
  return lines;
}

body = grid(840, 520);
body += `<polygon points="45,440 205,440 205,360" fill="white" stroke="#c43c39" stroke-width="4"/>`;
body += `<rect x="225" y="80" width="200" height="360" fill="#b7b7b7" stroke="#2866b1" stroke-width="4"/>`;
body += `<polygon points="445,440 805,440 625,240" fill="white" stroke="#c43c39" stroke-width="4"/>`;
body += `<polygon points="45,200 125,200 45,40" fill="#b7b7b7" stroke="#2866b1" stroke-width="4"/>`;
body += `<rect x="225" y="280" width="200" height="120" fill="white" stroke="#c43c39" stroke-width="4"/>`;
body += `<rect x="585" y="120" width="40" height="320" fill="#b7b7b7" stroke="#2866b1" stroke-width="4"/>`;
fs.writeFileSync(path.join(outDir, "shape-examples.svg"), svg(840, 520, body, "Shapes with different side counts, widths, heights, and standing classifications"));

body = grid(1000, 520, 50);
body += `<rect x="80" y="260" width="210" height="200" fill="white" stroke="#2866b1" stroke-width="4"/>`;
body += `<rect x="295" y="260" width="625" height="200" fill="white" stroke="#2866b1" stroke-width="4"/>`;
body += `<rect x="60" y="80" width="880" height="180" fill="#e7eef7" stroke="#2866b1" stroke-width="4"/>`;
for (let x = 60; x < 940; x += 40) body += `<line x1="${x}" y1="80" x2="${x + 180}" y2="260" stroke="#91add0" stroke-width="2"/>`;
body += `<polygon points="250,260 720,260 485,120" fill="white" stroke="#2866b1" stroke-width="4"/>`;
body += `<rect x="375" y="300" width="105" height="160" fill="white" stroke="#2866b1" stroke-width="4"/>`;
body += `<rect x="485" y="300" width="105" height="160" fill="white" stroke="#2866b1" stroke-width="4"/>`;
for (const x of [135, 180, 735, 780]) body += `<rect x="${x}" y="310" width="40" height="105" fill="white" stroke="#2866b1" stroke-width="4"/>`;
body += `<line x1="45" y1="462" x2="955" y2="462" stroke="#2866b1" stroke-width="5"/>`;
fs.writeFileSync(path.join(outDir, "standing-building.svg"), svg(1000, 520, body, "A wide building that is nevertheless described as standing architecture"));

for (const filename of fs.readdirSync(outDir).filter((name) => name.endsWith(".svg"))) {
  const source = path.join(outDir, filename);
  const destination = path.join(outDir, filename.replace(/\.svg$/, ".pdf"));
  execFileSync("/usr/bin/sips", ["-s", "format", "pdf", source, "--out", destination], { stdio: "ignore" });
}

console.log(`Wrote Chapter 1 figures to ${outDir}`);
