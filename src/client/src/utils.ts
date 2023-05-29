import { styleRuleList, currentText } from './rule_store';

export async function getStyleRules() {
    let response = await fetch("./rules", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    });

    let result = await response.json();

    let simplifiedRules = result.style_rules.map((rule, index) => {
        return {
            index,
            name: rule.name,
        };
    });

    styleRuleList.set(simplifiedRules);
}

export async function createStyleRule() {
    let currentTextValue = "";
    currentText.subscribe(value => { currentTextValue = value });
    let response = await fetch("./rules", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: currentTextValue,
        }),
    });

    response.status === 200 && (await getStyleRules());
    currentText.set("");

}

export async function deleteStyleRule(event) {
    const index = event.detail.index;

    let response = await fetch(`./rules/${index}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
    });

    response.status === 200 && (await getStyleRules());
}