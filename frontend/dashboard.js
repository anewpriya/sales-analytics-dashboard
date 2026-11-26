"use strict";
const h = React.createElement;
const {useEffect, useRef, useState} = React;
const fmt = n => n == null ? "—" : Number(n).toLocaleString("en-GB");
const pct = n => n == null ? "—" : n.toFixed(2) + "%";

function Card({title, children}) {
    return h("section", {className:"card"}, title && h("h2", null, title), children);
}

function Bar({labels, values, label, color}) {
    const ref = useRef(null);
    useEffect(() => {
        if (!window.Chart) return;
        const chart = new Chart(ref.current, {
            type:"bar",
            data:{labels,datasets:[{label,data:values,backgroundColor:color || "#176b77",borderRadius:4}]},
            options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
                scales:{y:{beginAtZero:true,grid:{color:"#e6edf2"}},x:{grid:{display:false}}}}
        });
        return () => chart.destroy();
    }, [labels, values, label, color]);
    return h("div",{className:"chart"},h("canvas",{ref,role:"img","aria-label":labels.map((l,i)=>l+": "+fmt(values[i])).join("; ")}));
}

function SegmentTable({groups}) {
    return h("div",{className:"table-wrap"},h("table",null,
        h("thead",null,h("tr",null,...["Segment","Accounts","Churned","Churn proportion"].map(x=>h("th",{key:x,scope:"col"},x)))),
        h("tbody",null,...groups.map(g=>h("tr",{key:g.label},h("td",null,g.label),h("td",null,fmt(g.total_customers)),h("td",null,fmt(g.churned_customers)),h("td",null,pct(g.churn_rate)))))));
}

function App() {
    const [login,setLogin] = useState("all");
    const [data,setData] = useState(null);
    const [error,setError] = useState("");
    useEffect(()=>{
        const controller = new AbortController();
        setData(null); setError("");
        fetch("/api/dashboard?login="+encodeURIComponent(login),{signal:controller.signal})
            .then(r=>{if(!r.ok) throw new Error("API request failed");return r.json();})
            .then(setData).catch(e=>{if(e.name!=="AbortError")setError("Could not load analytics. Check the Flask server and retry.");});
        return ()=>controller.abort();
    },[login]);
    const header=h("header",null,h("div",null,h("div",{className:"eyebrow"},"Product analytics / Portfolio"),h("h1",null,"Retention Intelligence"),h("p",{className:"muted"},"Customer behaviour, churn patterns and lifecycle opportunities.")),h("span",{className:"pill"},"Synthetic data · static snapshot"));
    const filter=h("div",{className:"toolbar"},h("label",null,"Login frequency ",h("select",{value:login,onChange:e=>setLogin(e.target.value)},...["all","Daily","Weekly","Rarely"].map(x=>h("option",{key:x,value:x},x==="all"?"All accounts":x)))),h("span",{className:"muted"},"Churn proportion = labelled churned / selected accounts"));
    if(!data) return h("main",null,header,filter,h("div",{className:"card"+(error?" error":""),role:error?"alert":"status"},error||"Loading analytics…"));
    const m=data.metrics, a=data.comparison.active, c=data.comparison.churned;
    const actions=[
        ["1. Re-engagement","First investigate low-usage accounts; test targeted outreach with consenting users.","14-day return rate; unsubscribes"],
        ["2. Product education","Test use-case tutorials for infrequent users.","30-day active retention; opt-outs"],
        ["3. Early activation","Explore onboarding friction before testing a contextual checklist for new accounts.","7-day activation; support contacts"]
    ];
    return h("main",null,header,filter,
        h("div",{className:"metrics"},...[["Accounts",fmt(m.total_customers)],["Active",fmt(m.active_customers)],["Churned",fmt(m.churned_customers)],["Churn proportion",pct(m.churn_rate)]].map(([k,v])=>h("section",{key:k,className:"card"},h("div",{className:"muted"},k),h("div",{className:"number"},v)))),
        h("div",{className:"callout"},h("h3",null,"What the data tells us"),...data.insights.map((x,i)=>h("p",{key:i},x)),login==="all"&&h("p",null,"Infrequent login accounts show 85.46% labelled churn versus 13.02% for daily login accounts. This is a prioritisation signal, not a causal finding.")),
        h("div",{className:"grid"},
            h(Card,{title:"Average daily usage (minutes)"},h(Bar,{labels:["Active","Churned"],values:[a.avg_daily_usage_mins,c.avg_daily_usage_mins],label:"Minutes",color:["#176b77","#b76b43"]}),h("p",{className:"muted"},"Active: "+fmt(a.avg_daily_usage_mins)+" · Churned: "+fmt(c.avg_daily_usage_mins))),
            h(Card,{title:"Login frequency"},h(SegmentTable,{groups:data.segments.login}))),
        h("div",{className:"grid"},h(Card,{title:"Account tenure"},h(SegmentTable,{groups:data.segments.tenure})),h(Card,{title:"Daily usage bands"},h(SegmentTable,{groups:data.segments.usage}))),
        h(Card,{title:"Proposed lifecycle experiments"},h("p",{className:"muted"},"Suggested order for investigation across the full sample, not proven impact. Validate audience size, feasibility and consent before testing."),h("div",{className:"actions"},...actions.map(([title,desc,metric])=>h("article",{key:title,className:"action"},h("h3",null,title),h("p",null,desc),h("small",{className:"muted"},metric))))),
        h("footer",{className:"footer"},"Portfolio prototype. No live customer data, causal claims or prospective risk predictions. The offline classification baseline is documented in the repository. ",h("a",{href:"https://github.com/anewpriya/sales-analytics-dashboard/blob/main/docs/CASE_STUDY.md"},"Read the product case study")," · ",h("a",{href:"https://github.com/anewpriya/sales-analytics-dashboard"},"Source code"))
    );
}
ReactDOM.createRoot(document.getElementById("root")).render(h(App));
