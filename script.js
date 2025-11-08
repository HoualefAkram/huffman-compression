class Node {
  constructor( rep, freq, left=null, right=null) {
        this.rep = rep;
        this.freq = freq;
        this.left = left;
        this.right = right;
  }

    toString() {
    return `(${this.rep}, ${this.freq}, left: ${this.left}, right: ${this.right})`;
    }
}

class Tree {
    constructor(nodes) {
        this.nodes = nodes;
    }

    toString() {
    return this.nodes.map(node => String(node)).join("\n");
    }

  sort() {
    this.nodes.sort((a, b) => a.freq - b.freq);
  }

  isMinimal() {
    return this.nodes.length === 1;
  }

  combineLastTwo() {
    const n1 = this.nodes[0];
    const n2 = this.nodes[1];

    this.nodes = this.nodes.filter(n => n !== n1 && n !== n2);

    this.nodes.push(
      new Node(`${n1.rep}-${n2.rep}`, n1.freq + n2.freq, n1, n2)
    );
  }
}


function frequency(text) {
  const result = {};
  for (const l of text) {
    if (result[l]) {
      result[l] += 1;
    } else {
      result[l] = 1;
    }
  }
  return result;
}


 function dfsPreorder(root, currentStr = "", code = {}) {
  if (root.left) {
    dfsPreorder(root.left, currentStr + "0", code);
  }

  if (root.right) {
    dfsPreorder(root.right, currentStr + "1", code);
  }

  if (!root.left && !root.right) {
    code[root.rep] = currentStr;
  }
  return code;
}

function encode(text, codeMap) {
    c = "";
    for (const t of text) {
        c = c + codeMap[t];
    }
    return c;
}


function generate() {
    let text = document.getElementById("text").value;

    let displayCode = document.getElementById("code");
    let displayMap = document.getElementById("map");

    const freq = frequency(text);
    const nodes = Object.entries(freq).map(([key, value]) => new Node(key, value));
    const tree = new Tree();
    tree.nodes = nodes;
    tree.sort();

    while (!tree.isMinimal()) {
    tree.combineLastTwo();
    tree.sort();
    }

    const codeMap = dfsPreorder(tree.nodes[0]);
    const code = encode(text,codeMap);  
    displayCode.textContent = `code: ${code}`;


    let table = document.getElementById("table");
    var i = 0;
    for (const [key, value] of Object.entries(codeMap)) {
        let row = table.insertRow(i);
        let col1 = row.insertCell(0);
        col1.textContent = key;
        let col2 = row.insertCell(1);
        col2.textContent = value;
        i=i+1;
    }
    // draw the graph
}







